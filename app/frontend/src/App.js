import './styles/App.css';
import { Button, Slider } from '@mui/material';
import { useState } from 'react';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import axios from 'axios'

function App() {

  const [var1, setVar1] = useState(50)
  const [var2, setVar2] = useState(50)
  const [var3, setVar3] = useState(50)
  const [var4, setVar4] = useState(50)
  const [var5, setVar5] = useState(50)

  const[open, setOpen] = useState(false)

  
  const sendData = () => {

    const data = {
      variable1: var1,
      variable2: var2,
      variable3: var3, 
      variable4: var4,
      variable5: var5
    }

    axios.post('link', {data})
      .then(res => {
        console.log(res)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return (
    <div className="App">
      <div className={open === true ? 'wrapper side-panel-open' : 'wrapper'}>
        <div className='main'>
          <h1>
            Main Content
          </h1>
        </div>
        <button className={open === true ? 'side-panel-toggle' : 'side-panel-toggle sp-open'} onClick={() => setOpen(!open)}>
          <span className='material-icons sp-icon-close'><ArrowBackIosIcon/></span>
          <span className='material-icons sp-icon-open'><ArrowForwardIosIcon/></span>
        </button>
        <div className='side-panel'>

          <div className={open === false ? 'side-content' : 'side-content content-closed'}>
            <h1>Variables</h1>
            <h3>
              Variable 1: <span className='value'>{var1}</span>
            </h3>
            <Slider
              onChange={(_, value) => setVar1(value)}
              defaultValue={50}
              aria-label='default'
              valueLabelDisplay='auto'
            />
            <h3>
              Variable 2: <span className='value'>{var2}</span>
            </h3>
            <Slider
              onChange={(_, value) => setVar2(value)}
              defaultValue={50}
              aria-label='default'
              valueLabelDisplay='auto'
            />
            <h3>
              Variable 3: <span className='value'>{var3}</span>
            </h3>
            <Slider
              onChange={(_, value) => setVar3(value)}
              defaultValue={50}
              aria-label='default'
              valueLabelDisplay='auto'
            />
            <h3>
              Variable 4: <span className='value'>{var4}</span>
            </h3>
            <Slider
              onChange={(_, value) => setVar4(value)}
              defaultValue={50}
              aria-label='default'
              valueLabelDisplay='auto'
            />
            <h3>
              Variable 5: <span className='value'>{var5}</span>
            </h3>
            <Slider
              onChange={(_, value) => setVar5(value)}
              defaultValue={50}
              aria-label='default'
              valueLabelDisplay='auto'
            />
            <div className='submit-button'>
              <Button
              onClick={sendData}
              variant='contained'>
                Submit
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
