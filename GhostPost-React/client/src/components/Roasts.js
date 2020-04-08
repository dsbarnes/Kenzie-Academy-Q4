import React from 'react'
import { Card, Button } from 'react-bootstrap'

function Roasts({ data, handleUpVote, handleDownVote }) {
  return (
    <div className='container'>

      {data &&
        data.filter(element => !element.is_boast)
          .map(element => {
            return (
              <React.Fragment>
                <Card className='mb-4'>
                  <Card.Body>
                    <small>Roast</small>
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
          })
      }
    </div>
  );
}

export default Roasts;