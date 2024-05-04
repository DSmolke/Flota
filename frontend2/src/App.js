const Input = ({type, id_, labelTxt, errorMsg, value, className}) => {
    return (
        <div className={className}>
            <label htmlFor={id_}>{labelTxt}</label>
            <input type={type} className="form-control is-valid" id={id_} value={value}/>
            {/*is-valid is-invalid ""*/}
            <div className="invalid-feedback">{errorMsg}</div>
        </div>
    )
}


const AddForm = () => {

    return <form>
        <div className="form-row">
            <Input
                type={"text"}
                id_={"first_name"}
                labelTxt={"First name:"}
                errorMsg={"Please enter your first name."}
                className="form-group col-md-4"
                value={""}
            />
            <Input
                type={"text"}
                id_={"last_name"}
                labelTxt={"Last name:"}
                errorMsg={"Please enter your last name."}
                className="form-group col-md-4"
                value={""}
            />
            <Input
                type={"email"}
                id_={"email"}
                labelTxt={"Email:"}
                errorMsg={"Please enter a valid email."}
                className="form-group col-md-4"
                value={""}
            />
            <Input
                type={"text"}
                id_={"phone_number"}
                labelTxt={"Phone number:"}
                errorMsg={"Please enter a valid phone number."}
                className="form-group col-md-4"
                value={""}
            />
            <Input
                type={"text"}
                id_={"car_registration"}
                labelTxt={"Car registration:"}
                errorMsg={"Please enter car registration."}
                className="form-group col-md-4"
                value={""}
            />
            <div className="form-group col-md-4">
                <button className="btn btn-success mt-3">Add</button>
            </div>
        </div>
    </form>
}

const SearchBar = () => {
    return (
        <div className="row mt-4">
            <div className="col-md-6">
                <div className="input-group">
                    <input type="text" className="form-control" placeholder="Search..." aria-label="Search"/>
                </div>
            </div>
        </div>
    )
}

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

    const ElementRow = ({values, id_}) => {
        return (
            <tr>
                {
                    values.map(value => <td>{value}</td>)
                }
                <td>
                    <button className="btn btn-success">Edit {id_}</button>
                </td>
            </tr>
        )
    }

    return (
        <table className="table">
            <Headers names={["First name", "Last name", "Email", "Phone number", "Car registration", ""]}/>
            <tbody>
            <ElementRow values={["Damian", "Smolczyński", "d.smolczynski1@gmail.com", "570688764", "WZ275EL"]} id_={1}/>
            </tbody>
        </table>
    )
}


const Panel = () => {
    return <div className="container">
        <h1>Drivers panel</h1>
        <p>Once you'll add a driver, he will be notified about upcoming deadlines for his car.</p>

        <AddForm/>
        <SearchBar/>
        <ElementsTable/>

    </div>
}

const EditForm = () => {
    return <div className="container mt-4">
        <div className="row justify-content-center">
            <div className="col-md-6">
                <div className="card">
                    <div className="card-header">Edit Object</div>
                    <div className="card-body">
                        <form>
                            <Input
                                type={"text"}
                                id_={"first_name"}
                                labelTxt={"First name:"}
                                errorMsg={"Please enter your first name."}
                                className="mb-3"
                                value={"Damian"}
                            />
                            <Input
                                type={"text"}
                                id_={"last_name"}
                                labelTxt={"Last name:"}
                                errorMsg={"Please enter your last name."}
                                className="mb-3"
                                value={"Smolczński"}
                            />
                            <Input
                                type={"email"}
                                id_={"email"}
                                labelTxt={"Email:"}
                                errorMsg={"Please enter a valid email."}
                                className="mb-3"
                                value={"d.smolczynski1@gmail.com"}
                            />
                            <Input
                                type={"text"}
                                id_={"phone_number"}
                                labelTxt={"Phone number:"}
                                errorMsg={"Please enter a valid phone number."}
                                className="mb-3"
                                value={"570688764"}
                            />
                            <Input
                                type={"text"}
                                id_={"car_registration"}
                                labelTxt={"Car registration:"}
                                errorMsg={"Please enter car registration."}
                                className="mb-3"
                                value={"WZ295EL"}
                            />
                            <button type="submit" className="btn btn-primary">Save</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
}
const App = () => {
    return (
        <>
            <Panel/>
            <EditForm/>
        </>
    )
}

export default App


