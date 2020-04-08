import React from 'react'
import { Card, Button } from 'react-bootstrap'

function AllPosts({ data, handleUpVote, handleDownVote }) {
  return (
    <div className='container'>

      {data && data.map(element => {
        return (
          <React.Fragment>
            <Card className='mb-4'>
              <Card.Body>
                {element.is_boast ?
                  <small>Boast</small> :
                  <small>Roast</small>
                }

                <Card.Text>{element.contents}</Card.Text>

                <div className='buttonGroup'>
                  <Button
                    variant='primary'
                    onClick={() => handleUpVote(element.pk)}
                  >
                    ({element.up_votes}) Like
                  </Button>

                  <Button
                    variant='danger'
                    onClick={() => handleDownVote(element.pk)}
                  >
                    ({element.down_votes}) Dislike
                  </Button>
                </div>

              </Card.Body>
            </Card>
          </React.Fragment>
        )
      })}
    </div>
  );
}

export default AllPosts;