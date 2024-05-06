// Panel.js ma za zadanie połączenie formularza dodawania kierowcy,
// wraz z ich tabelą, którą można sortować po wartości wpisywanej w
// pasku wyszukiwania


import {useEffect, useState} from "react";
import {createPortal} from "react-dom"
import React from "react";

// funkcja pomocnicza do sprawdzania, czy regex jest ok
const matchesRegex = (regex, expression) => {
    return regex.test(expression)
}

const carRegexes = {
    firstName: /^[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{1,20}$/,
    lastName: /^[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{1,30}(-[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{1,30})?$/,
    email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
    phoneNumber: /^[0-9]{9}$/,
    carRegistration: /^[A-Z0-9]{7}$/
}
const carErrorMessages = {
    firstName: "Enter valid first name",
    lastName: "Enter valid last name",
    email: "Enter valid email",
    phoneNumber: "Enter valid phone number",
    carRegistration: "Enter valid car registration"
}
const carFormInitialState =  {
    firstName: "",
    lastName: "",
    email: "",
    phoneNumber: "",
    carRegistration: ""
}
const carFormInitialErrors = {
    firstName: null,
    lastName: null,
    email: null,
    phoneNumber: null,
    carRegistration: null
}

const AddForm = ({setChange}) => {
    const regexes = {...carRegexes}
    const errorMessages = {...carErrorMessages}
    const [formData, setFormData] = useState({...carFormInitialState})
    const [errors, setErrors] = useState({...carFormInitialErrors})
    const [postError, setPostError] = useState(false)
    const handleErrors = (name, value) => {
        if (matchesRegex(regexes[name], value)) {
            setErrors({...errors, [name]: null})
        } else {
            setErrors({...errors, [name]: errorMessages[name]})
        }
    }

    const handleChange = (e) => {
        const {name, value} = e.target
        setFormData({...formData, [name]: value})
        handleErrors(name, value)
    }

    const onSubmit = async (e) => {
        e.preventDefault();
        if (!(errors.firstName || errors.lastName || errors.email || errors.phoneNumber || errors.carRegistration)) {
            await fetch("http://localhost:8008/driver",
                {
                    method: "POST",
                    body: JSON.stringify(
                        {"first_name": formData.firstName,
                            "last_name": formData.lastName,
                            "email": formData.email,
                            "phone_number": formData.phoneNumber,
                            "car_registration": formData.carRegistration
                        }),
                    headers:{"content-type": "application/json"}}
            ).then(res => {
                if (res.status === 201) {
                    setChange(true);
                    setPostError(false);
                    setFormData({...carFormInitialState})
                }
                if (res.status === 403) {
                    setPostError(true)
                }
            })
        }

        }

    return <form onSubmit={onSubmit}>
        <div className="form-row">
            {/*-------------[ First name ] ---------------*/}
            <div className="form-group col-md-4">
                <label htmlFor="firstName">First name:</label>
                <input type="text" className="form-control" id="firstName" name="firstName" value={formData.firstName}
                       onChange={handleChange}/>
                {errors.firstName && <div style={{color: "red"}}>{errors.firstName}</div>}
            </div>

            {/*/!*-------------[ Last name ] ---------------*!/*/}
            <div className="form-group col-md-4">
                <label htmlFor="lastName">Last name:</label>
                <input type="text" className="form-control" id="lastName" name="lastName" value={formData.lastName}
                       onChange={handleChange}/>
                {errors.lastName && <div style={{color: "red"}}>{errors.lastName}</div>}
            </div>
            {/*/!*-------------[ Email ] ---------------*!/*/}
            <div className="form-group col-md-4">
                <label htmlFor="email">Email:</label>
                <input type="text" className="form-control" id="email" name="email" value={formData.email}
                       onChange={handleChange}/>
                {errors.email && <div style={{color: "red"}}>{errors.email}</div>}
            </div>
            {/*/!*-------------[ Phone number ] ---------------*!/*/}
            <div className="form-group col-md-4">
                <label htmlFor="phoneNumber">Phone number:</label>
                <input type="text" className="form-control" id="phoneNumber" name="phoneNumber"
                       value={formData.phoneNumber}
                       onChange={handleChange}/>
                {errors.phoneNumber && <div style={{color: "red"}}>{errors.phoneNumber}</div>}
            </div>

            {/*/!*-------------[ Car registration ] ---------------*!/*/}
            <div className="form-group col-md-4">
                <label htmlFor="carRegistration">Car registration:</label>
                <input type="text" className="form-control" id="carRegistration" name="carRegistration" value={formData.carRegistration}
                       onChange={handleChange}/>
                {errors.carRegistration && <div style={{color: "red"}}>{errors.carRegistration}</div>}
            </div>

            {postError && <div style={{color: "red"}}>Duplicate entry!</div>}
            <div className="form-group col-md-4">
                <button type={"submit"} className="btn btn-success mt-3">Add</button>
            </div>
        </div>
    </form>
}


// --------------------------------- [ PORTAL EDYCJI ] ----------------------------------------------
const EditForm = ({setChange, driver, onClose}) => {
    const regexes = {...carRegexes}
    const errorMessages = {...carErrorMessages}
    const [formData, setFormData] = useState({
        firstName: driver.first_name,
        lastName: driver.last_name,
        email: driver.email,
        phoneNumber: driver.phone_number,
        carRegistration: driver.car_registration
    })
    const [errors, setErrors] = useState({...carFormInitialErrors})
    const [postError, setPostError] = useState(false)
    const handleErrors = (name, value) => {
        if (matchesRegex(regexes[name], value)) {
            setErrors({...errors, [name]: null})
        } else {
            setErrors({...errors, [name]: errorMessages[name]})
        }
    }

    const handleChange = (e) => {
        const {name, value} = e.target
        setFormData({...formData, [name]: value})
        handleErrors(name, value)
    }

    const onSubmit = async (e) => {
        e.preventDefault();
        if (!(errors.firstName || errors.lastName || errors.email || errors.phoneNumber || errors.carRegistration)) {
            await fetch(`http://localhost:8008/driver/${driver.id}`,
                {
                    method: "PATCH",
                    body: JSON.stringify(
                        {"first_name": formData.firstName,
                            "last_name": formData.lastName,
                            "email": formData.email,
                            "phone_number": formData.phoneNumber,
                            "car_registration": formData.carRegistration
                        }),
                    headers:{"content-type": "application/json"}}
            ).then(res => {
                if (res.status === 200) {
                    setChange(true);
                    setPostError(false);
                    setFormData({...carFormInitialState})
                    onClose()
                }
                if (res.status === 400 || res.status === 404) {
                    setPostError(true)
                }
            })
        }

    }
    return (<div className="container mt-4">
        <div className="row justify-content-center">
            <div className="col-md-6">
                <div className="card">
                    <div className="card-header">Edit Object</div>
                    <div className="card-body">
                        <form onSubmit={onSubmit}>
                            <div className="mb-3">
                                <label htmlFor="firstName">First name:</label>
                                <input type="text" className="form-control" id="firstName" name="firstName"
                                       value={formData.firstName}
                                       onChange={handleChange}/>
                                {errors.firstName && <div style={{color: "red"}}>{errors.firstName}</div>}
                            </div>
                            <div className="mb-3">
                                <label htmlFor="lastName">Last name:</label>
                                <input type="text" className="form-control" id="lastName" name="lastName"
                                       value={formData.lastName}
                                       onChange={handleChange}/>
                                {errors.lastName && <div style={{color: "red"}}>{errors.lastName}</div>}
                            </div>
                            <div className="mb-3">
                                <label htmlFor="email">Email:</label>
                                <input type="text" className="form-control" id="email" name="email"
                                       value={formData.email}
                                       onChange={handleChange}/>
                                {errors.email && <div style={{color: "red"}}>{errors.email}</div>}
                            </div>
                            <div className="mb-3">
                                <label htmlFor="phoneNumber">Phone number:</label>
                                <input type="text" className="form-control" id="phoneNumber" name="phoneNumber"
                                       value={formData.phoneNumber}
                                       onChange={handleChange}/>
                                {errors.phoneNumber && <div style={{color: "red"}}>{errors.phoneNumber}</div>}
                            </div>
                            <div className="mb-3">
                                <label htmlFor="carRegistration">Phone number:</label>
                                <input type="text" className="form-control" id="carRegistration" name="carRegistration"
                                       value={formData.carRegistration}
                                       onChange={handleChange}/>
                                {errors.carRegistration && <div style={{color: "red"}}>{errors.carRegistration}</div>}
                            </div>
                            {postError && <div style={{color: "red"}}>Invalid entry!</div>}
                            <button type="submit" className="btn btn-primary">Save</button>
                            <button className="btn btn-warning float-end" onClick={onClose}>Close</button>
                </form>
            </div>
        </div>
            </div>
        </div>
    </div>)
}
const EditPortal = ({isOpen, onClose, setChange, driver}) => createPortal(
    isOpen && <EditForm setChange={setChange} driver={driver} onClose={onClose}/>, document.getElementById('root')
)


// --------------------------------- [ PANEL ] ----------------------------------------------
const Panel = () => {
    const [drivers, setDrivers] = useState([])
    const [searchValue, setSearchValue] = useState("")
    const [change, setChange] = useState(true)

    {/*-------------[ Pobieranie wszystkich driverów ] ---------------*/
    }
    useEffect(() => {
        fetch("http://localhost:8008/drivers/all").then((response) => response.json()).then((data) => {
            console.log(data)
            setDrivers(data)
            setChange(false)
       })
    }, [change]);
    const ElementsTable = () => {
        const Headers = ({names}) => {
            const Header = ({name}) => {
                return <th scope="col">{name}</th>
            }

            return (
                <thead>
                <tr>
                    {
                        names.map(header => <Header name={header}/>)
                    }
                </tr>
                </thead>
            )
        }

        const DriverRow = ({driver}) => {
            const [modal, setModal] = useState(false)

            const handleDelete = async () => {
                if (window.confirm("Driver will be deleted permanently, are you positive to continue?")) {
                    await fetch(`http://localhost:8008/driver/${driver.id}`, {method: "DELETE"})
                    setChange(true)
                }

            }

            return (
                <tr>
                    <td>{driver.first_name}</td>
                    <td>{driver.last_name}</td>
                    <td>{driver.email}</td>
                    <td>{driver.phone_number}</td>
                    <td>{driver.car_registration}</td>
                    <td>
                        <button onClick={() => setModal(true)} className="btn btn-success">Edit {driver.id}</button>
                        <EditPortal driver={driver} setChange={setChange} isOpen={modal} onClose={() => setModal(false)} />
                    </td>
                    <td>
                        <button onClick={handleDelete} className="btn btn-warning">Delete {driver.id}</button>

                    </td>
                </tr>
            )
        }


        return (
            <table className="table">
                <Headers names={["First name", "Last name", "Email", "Phone number", "Car registration", ""]}/>
                <tbody>
                {
                    searchValue ?
                        drivers
                            .filter((driver) => Object.values(driver).join(', ').toUpperCase().includes(searchValue.toUpperCase()))
                            .map(driver => <DriverRow driver={driver} key={driver.id}/>)
                        : drivers.map(driver => <DriverRow driver={driver} key={driver.id}/>)
                }
                </tbody>
            </table>
        )
    }


    const SearchBar = () => {
        return (
            <div className="row mt-4">
                <div className="col-md-6">
                    <div className="input-group">
                        <input type="text" className="form-control" aria-label="Search" value={searchValue}
                               onChange={(e) => setSearchValue(e.target.value)}/>
                    </div>
                </div>
            </div>
        )
    }


    {/*-------------[ Cała logika łączy się w renderowanym komponencie ] ---------------*/}
    return <div className="container">
        <h1>Drivers panel</h1>
        <p>Once you'll add a driver, he will be notified about upcoming deadlines for his car.</p>
        <AddForm setChange={setChange}/>

        {/*-------------[ Search bar ] ---------------*/}
        <SearchBar/>
        {/*-------------[ Wszyscy driverzy przefiltrowani po wartości seach bara jeżeli jest różna od "" ] ---------------*/}
        <ElementsTable/>

    </div>
}

export default Panel