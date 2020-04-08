import json
import os
import shutil
from shutil import copy
from typing import List, Dict

filename = "chapter2.txt"


def load_data_from_file(path=None) -> str:
    """
    Returns a str
    reads a tile from 'path' and returns the data from that file
    """
    with open(path if path else filename, 'r') as f:
        data = f.read()
    return data


class ShardHandler(object):
    """
    Take any text file and shard it into X number of files with
    Y number of replications.
    """
    mapfile = "mapping.json"

    def __init__(self):
        self.mapping = self.load_map()
        self.last_char_position = 0

    def load_map(self) -> Dict:
        """
        Load the 'database' mapping from file. (mapping.json)
        Turns a JSON file into a python object
        """
        if not os.path.exists(self.mapfile):
            return dict()
        with open(self.mapfile, 'r') as m:
            return json.load(m)

    def write_map(self) -> None:
        """
        Write the current 'database' (json file) to file.
        load_map has run on mapping.json (see __init__)
        json.dumps formats the python object into a string
        """
        with open(self.mapfile, 'w') as JSONfile:
            json.dump(self.mapping, JSONfile, indent=2)

    def _reset_char_position(self):
        self.last_char_position = 0

    def get_shard_ids(self) -> List[int]:
        return sorted([key for key in self.mapping.keys() if '-' not in key])

    def get_replication_ids(self) -> List[int]:
        return sorted([key for key in self.mapping.keys() if '-' in key])


    def _generate_sharded_data(self, count: int, data: str) -> List[str]:
        """
        Split the data into as many pieces as needed.
        The -> List[str] are the sub strings of the text file
        that will now make up the values in our db obj
        """
        splicenum, rem = divmod(len(data), count)

        # Don't think about this at all - it works as it should.
        result = [data[splicenum * z:splicenum * (z + 1)] for z in range(count)]
        # take care of any odd characters
        if rem > 0:
            result[-1] += data[-rem:]

        return result

    def build_shards(self, count: int, data: str = None) -> [str, None]:
        """Initialize our miniature databases from a clean mapfile. Cannot
        be called if there is an existing mapping -- must use add_shard() or
        remove_shard()."""
        if self.mapping != {}:
            return "Cannot build shard setup -- sharding already exists."

        # gen_shard_data -> List[str]
        spliced_data = self._generate_sharded_data(count, data)

        for num, d in enumerate(spliced_data):
            # Writes an individual shard to disk
            self._write_shard(num, d)

        self.write_map()

    def _write_shard_mapping(self, num: str, data: str, replication=False):
        """
        Write the requested data to the mapfile. The optional `replication`
        flag allows overriding the start and end information with the shard
        being replicated.
        This function is run in _write_shard and it what adds a shard to the mapping.
        """
        if replication:
            parent_shard = self.mapping.get(num[:num.index('-')])
            self.mapping.update(
                {
                    num: {
                        'start': parent_shard['start'],
                        'end': parent_shard['end']
                    }
                }
            )
        else:
            if int(num) == 0:
                # We reset it here in case we perform multiple write operations
                # within the same instantiation of the class. The char position
                # is used to power the index creation.
                self._reset_char_position()

            self.mapping.update(
                {
                    str(num): {
                        'start': (
                            self.last_char_position if
                            self.last_char_position == 0 else
                            self.last_char_position + 1
                        ),
                        'end': self.last_char_position + len(data)
                    }
                }
            )

            self.last_char_position += len(data)

    def _write_shard(self, num: int, data: str) -> None:
        """Write an individual database shard to disk and add it to the
        mapping."""
        if not os.path.exists("data"):
            os.mkdir("data")
        with open(f"data/{num}.txt", 'w') as s:
            s.write(data)
        self._write_shard_mapping(str(num), data)

    def load_data_from_shards(self) -> str:
        """Grab all the shards, pull all the data, and then concatenate it."""
        result = list()

        for db in self.get_shard_ids():
            with open(f'data/{db}.txt', 'r') as f:
                result.append(f.read())
        return ''.join(result)

    def add_shard(self) -> None:
        """Add a new shard to the existing pool and rebalance the data."""
        self.mapping = self.load_map()
        # load_data_from_shards -> str
        data = self.load_data_from_shards()

        # get_shard_ids -> List[int]
        keys = [int(z) for z in self.get_shard_ids()]
        keys.sort()

        # why 2? Because we have to compensate for zero indexing
        new_shard_num = max(keys) + 2

        # gen_sharded_data -> List[str]
        spliced_data = self._generate_sharded_data(new_shard_num, data)

        for num, d in enumerate(spliced_data):
            self._write_shard(num, d)

        self.write_map()

        # self.sync_replication()

    def remove_shard(self) -> None:
        """Loads the data from all shards, removes the extra 'database' file,
        and writes the new number of shards to disk.
        """

        for f in os.listdir(os.path.join(os.getcwd(), 'data/')):
            os.remove(os.path.join(os.getcwd(), 'data', f))

        number_of_shards = len(self.get_shard_ids()) - 1

        # load_data_from_file -> str
        chapter = load_data_from_file()

        self.mapping = {}
        self.build_shards(number_of_shards, chapter)

        try:
            new_shard_num = (number_of_shards)
        except ValueError:
            raise Exception('goofed')

        self.write_map()

        # self.sync_replication()

    def add_replication(self) -> None:
        """Add a level of replication so that each shard has a backup. Label
        them with the following format:

        1.txt (shard 1, primary)
        1-1.txt (shard 1, replication 1)
        1-2.txt (shard 1, replication 2)
        2.txt (shard 2, primary)
        2-1.txt (shard 2, replication 1)
        ...etc.

        By default, there is no replication -- add_replication should be able
        to detect how many levels there are and appropriately add the next
        level.
        """
        try:
            replication_level = 0

            for foo in os.listdir(os.path.join(os.getcwd(), 'data')):

                index = foo.find('-')
                level_check = int(foo[index + 1:foo.find('.')]) if index != -1 else - 1

                if index > 0 and level_check > replication_level:
                    replication_level = level_check

                end_of_filename = int(foo.find('.'))

                full_filename = os.path.join(os.getcwd(), 'data', foo)
                filename_no_ext = os.path.join(os.getcwd(), 'data', foo[0:end_of_filename])

                pass_as_num = f"{foo[:-4]}-{replication_level + 1}"
                new_filename = f"{filename_no_ext}-{replication_level + 1}.txt"

                if '-' not in foo:
                    self._write_shard_mapping(pass_as_num, '', replication=True)
                    shutil.copyfile(full_filename, new_filename)
                
            self.write_map()

        except FileNotFoundError:
            raise "Fuck."

    def remove_replication(self) -> None:
        """Remove the highest replication level.

        If there are only primary files left, remove_replication should raise
        an exception stating that there is nothing left to remove.

        For example:

        1.txt (shard 1, primary)
        1-1.txt (shard 1, replication 1)
        1-2.txt (shard 1, replication 2)
        2.txt (shard 2, primary)
        etc...

        to:

        1.txt (shard 1, primary)
        1-1.txt (shard 1, replication 1)
        2.txt (shard 2, primary)
        etc...
        """
        try:
            replication_level = 0

            for foo in os.listdir(os.path.join(os.getcwd(), 'data')):
                index = foo.find('-')
                level_check = int(foo[index + 1:foo.find('.')]) if index != -1 else - 1

                if index > 0 and level_check > replication_level:
                    replication_level = level_check

            for bar in os.listdir(os.path.join(os.getcwd(), 'data')):
                
                if f'-{replication_level}.txt' in bar:
                    os.remove(os.path.join(os.getcwd(), 'data', bar))
                    index = bar.find('-')
                    del self.mapping[f'{bar[0:index]}-{replication_level}']

        except FileNotFoundError:
            raise "Fuck."

    def sync_replication(self) -> None:
        """Verify that all replications are equal to their primaries and that
        any missing primaries are appropriately recreated from their
        replications."""
        try:
            primaries = self.get_shard_ids()
            backups = self.get_replication_ids()
            highest_rep_level = max([int(x[x.index('-') + 1:]) for x in backups])

            for n in primaries:
                for num in range(highest_rep_level + 1):
                    if str(n) + '-' + str(num) not in backups:
                        copy(f'data/{n}', f'data/{n}-{num}')

        except FileNotFoundError:
            raise "Fuck."

    def get_shard_data(self, shardnum=None) -> [str, Dict]:
        """Return information about a shard from the mapfile."""
        if not shardnum:
            return self.get_all_shard_data()
        data = self.mapping.get(shardnum)
        if not data:
            return f"Invalid shard ID. Valid shard IDs: {self.get_shard_ids()}"
        return f"Shard {shardnum}: {data}"

    def get_all_shard_data(self) -> Dict:
        """A helper function to view the mapping data."""
        return self.mapping


s = ShardHandler()

# s.build_shards(5, load_data_from_file())
# print(s.mapping.keys())

# s.add_shard()
# print(s.mapping.keys())

# s.remove_shard()
# print(s.mapping.keys())

# s.add_replication()
# print(s.mapping.keys())

# s.remove_replication()
# print(s.mapping.keys())
