import { useState } from 'react'
import './App.css'

function App() {
  const [movie, setmovie] = useState("")
  const [recommendations, setRecommendations] = useState({ top: [], poster: [] })

  async function find(movie) {
    let req = await fetch(`http://127.0.0.1:5000/${movie}`)
    let res = await req.json()
    setRecommendations({ top: res.top, poster: res.poster })
    console.log(res)
  }

  return (
    <>
      <h1>🎬Netflix Tv Shows & Movie Recommendation System</h1>
      <input
        type="text"
        onChange={(e) => setmovie(e.target.value)}
        placeholder='Enter the Movie Name'
        className='input'
      />
      <button onClick={() => find(movie)} className='btn'>Submit</button>

<div className='flex' >
      {recommendations.top.length > 0 && (
        <ol>
          {recommendations.top.map((item, index) => (
            <li key={index}>
              <p>{item}</p>
              <img
                src={recommendations.poster[index]}
                alt={`Poster of ${item}`}
                style={{ width: '200px', marginBottom: '10px' }}
              />
            </li>
          ))}
        </ol>
      )}
      </div>
    </>
  )
}

export default App
