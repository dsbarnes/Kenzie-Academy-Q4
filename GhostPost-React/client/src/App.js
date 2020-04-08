import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { AllPosts, Boasts, Roasts, NewPostForm } from './components'

function App() {

  const [allPosts, setAllPosts] = useState(null)
  const [refresher, setRefresher] = useState(0)

  useEffect(() => {
    fetch('http://localhost:8000/api/posts/')
      .then(res => res.json())
      .then(djangoData => setAllPosts([...djangoData]))
  }, [refresher])

  const handleUpVote = (id) => {
    const url = `http://localhost:8000/api/posts/${id}/vote_up/`
    fetch(url, { method: 'POST' })
      .then(setRefresher(refresher - 1))
  }
  const handleDownVote = (id) => {
    const url = `http://localhost:8000/api/posts/${id}/vote_down/`
    fetch(url, { method: 'POST' })
      .then(setRefresher(refresher - 1))
  }
  const handleSort = async () => {
    const sortedData = await allPosts.sort((cur, nxt) => {
      return (nxt.up_votes - nxt.down_votes) - (cur.up_votes - cur.down_votes)
    })
    setAllPosts([...sortedData])
  }

  return (
    <React.Fragment>

      <Router>
        <div className='menu ml-3' style={{ "display": "flex" }}>
          <p className='m-4'><Link to='/'>All</Link></p>
          <p className='m-4'><Link to='/boasts'>Boasts</Link></p>
          <p className='m-4'><Link to='/roasts'>Roasts</Link></p>
          <p className='m-4'><Link to='/newpost'>New Post</Link></p>
          <Button
            variant="outline-warning"
            className='m-3 ml-5'
            onClick={handleSort}
          >
            .sort( (a, b) => b - a);
          </Button>
        </div>

        <Switch>
          <div className='container'>
            <Route exact path='/'>
              <AllPosts
                data={allPosts}
                handleUpVote={handleUpVote}
                handleDownVote={handleDownVote}
              />
            </Route>

            <Route exact path='/boasts'>
              <Boasts
                data={allPosts}
                handleUpVote={handleUpVote}
                handleDownVote={handleDownVote}
              />
            </Route>

            <Route exact path='/roasts'>
              <Roasts
                data={allPosts}
                handleUpVote={handleUpVote}
                handleDownVote={handleDownVote}
              />
            </Route>

            <Route exact path='/newpost'>
              <NewPostForm data={allPosts} />
            </Route>

          </div>
        </Switch>
      </Router>
    </React.Fragment >
  );
}

export default App;
