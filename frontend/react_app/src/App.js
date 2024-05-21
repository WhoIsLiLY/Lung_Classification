// src/App.js
import React, { useState } from 'react';
import './App.css';

function App() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://127.0.0.1:5000/classify-image', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            setResult(data.result);
        } catch (error) {
            console.error('Error:', error);
            setResult('An error occurred');
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Image Classification</h1>
                <form onSubmit={handleSubmit}>
                    <input type="file" onChange={handleFileChange} />
                    <button type="submit">Upload and Classify</button>
                </form>
                {result && <p>{result}</p>}
            </header>
        </div>
    );
}

export default App;
