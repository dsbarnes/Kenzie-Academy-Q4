import React, { useState } from 'react'
import {
  Form,
  InputGroup,
  ToggleButtonGroup,
  ToggleButton,
  Button
} from 'react-bootstrap'


function NewPostForm({ data }) {
  const [error, setError] = useState(null)
  const [success, setSuccess] = useState(null)
  const [charCount, setCharCount] = useState(0)

  const countChars = (e) => {
    setCharCount(e.target.value.length)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const formData = e.target.elements
    const is_boast = formData[1].checked
    const contents = formData[0].value
    const submission_time = new Date().toISOString()
    const errorEmptyContent = 'Cannot Post an Empty Roast or Boast'
    const errorContentToLong = 'Limit of 280 characters'

    if (contents.length === 0) setError(errorEmptyContent)
    if (contents.length > 280) setError(errorContentToLong)

    const postData = {
      is_boast: is_boast,
      contents: contents,
      submission_time: submission_time
    }

    fetch('http://localhost:8000/api/posts/', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postData)
    })
      .then(res => {
        if (res.status === 201) {
          formData[0].value = ""
          setSuccess("Yay! You posted!")
        }
        else {
          formData[0].value = ""
          setError("Something went wrong")
        }
      })
  }

  return (
    <Form onSubmit={handleSubmit}>
      {error && <p className='text-danger'>{error}</p>}
      {success && <p className='text-success'>{success}</p>}

      <Form.Group controlId="exampleForm.ControlTextarea1">

        <Form.Label>Post a Roast or Boast:</Form.Label>

        <Form.Control as="textarea" onChange={(e) => countChars(e)} rows="3" />

        <small>{charCount} / 280</small>

        <InputGroup.Append className='mb-5'>
          <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
            <ToggleButton value={1}>Boast</ToggleButton>
            <ToggleButton variant='danger' value={2}>Roast</ToggleButton>
          </ToggleButtonGroup>
        </InputGroup.Append>

        <Button type='submit'>Submit</Button>
      </Form.Group>
    </Form>
  );
}

export default NewPostForm