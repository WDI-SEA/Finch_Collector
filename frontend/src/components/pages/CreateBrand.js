import React, { useState, useEffect } from 'react'
import { Form, Button, Card } from 'react-bootstrap'

const CreateBrand = (props) => {
    const [brands, setBrands] = useState([])

    useEffect(()=> {
        getBrands()
    }, [])
    const getBrands = () => {
        fetch('http://localhost:8000/brands/')
            .then(res => res.json())
            .then(foundBrands => {
                console.log('Found Brands by INDEX', foundBrands.brands)
                setBrands(foundBrands.brands)
            })
            .catch(err => console.log(err))
        }
        return (
            <div>
    
                <h1>Test</h1>
                {
                brands.map(brand => (
                    <li>
                        {brand.name}
                    </li>
                ))
                }  
            </div>
        
        )
}

export default CreateBrand