import React,{useRef,useState} from 'react';
import {SketchField,Tools} from 'react-sketch'
import {Alert, Button} from 'react-bootstrap'
import {saveAs} from 'file-saver'
import axios from 'axios'


const styles={
    draw: {
        margin:'0 auto'
    }
    
}


const Draw =() => {
    const [send,setSend]= useState(false)
    const [result,setResult]= useState()
    const sketch =useRef()
    const handleSumbit = ()=>{
        const canvas = sketch.current.toDataURL()
        // saveAs(canvas,'digit.jpg')
        sendData(canvas)

    }
    
    const handleReset= ()=>{
       sketch.current.clear()
       sketch.current._backgroundColor('black')
       setSend(false)
    }
    
    const sendData = (c)=>{
        console.log(c)
        const headers ={
            'accept':'application/json'
        }
        const fd = new FormData()
        fd.append('image',c)

        axios.post('http://127.0.0.1:8000/api/digits/',fd ,{headers:headers})
        .then(res=>{
            console.log(res.data)
            setSend(true)
            getImageResult(res.data.id)
        })
        .catch(err=>console.log(err))

    }

    const getImageResult = (id)=>{
        axios.get(`http://127.0.0.1:8000/api/digits/${id}/`)
        .then(res=>
            {
                setResult(res.data.result)
            })

    }
    return(
        <React.Fragment>
            {send && <Alert variant="info">Succeesfully sent for classification</Alert>}
            {result && <h3>Result is {result}</h3>}
            <SketchField
              ref={sketch}
              width='600px'
              height='600px'
              style={styles.draw}
              tool = {Tools.Pencil}
              backgroundColor='black'
              lineColor='white'
              imageFormat='jpg'
              lineWidth={30}
              />

            <div className='mt-4'>
                <Button onClick={handleSumbit} variant='primary'>Send</Button>
                <Button onClick={handleReset} variant='secondary'>Reset</Button>

            </div>
        </React.Fragment>
    );
}

export default Draw;