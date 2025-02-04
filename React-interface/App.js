import api from './api'
import {useState,useRef} from 'react'
import './style.css'

function App(){

   const inputid = useRef()
   const inputnome = useRef()

    const[nomes,setnomes] = useState([])

   async function get_nome(){
       const nomesapi = await api.get('/nome')
       setnomes(nomesapi.data)
    }

    async function post_nome(){
        await api.post('/nome',{
            id: inputid.current.value,
            nome: inputnome.current.value
        })
        get_nome()
    }

    async function delete_nome(id, nome) {
        await api.delete('/nome',{
            data: { id: id,
                nome: nome}
        })
        get_nome()
    }

    async function put_nome() {
        await api.put('/nome',{
            id: inputid.current.value,
            nome: inputnome.current.value
        })
        get_nome()
    }

    return (
        <>
        <center>
        <div>
            <form>
                <input type="text" name="ID" id="nID" ref={inputid} className='input-text' placeholder='ID'/>
                <br />
                <input type="text" name="name" id="name" ref={inputnome} className='input-text' placeholder='Nome'/>
                <br />
                <button type="button" className='button-post' onClick={post_nome}>List Add</button>
            </form>    
        </div>
        <br />
        <br />
        <div className='div-button'>
        <button type="button" className='button-get' onClick={get_nome}>Open List</button>
        </div>
        <table className='styled-table' id='table-rows'>
            <tbody>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>    
                </tr>
         {nomes.map((nome) => (
                <tr>
                    <td>{nome.id}</td>
                    <td>{nome.nome}</td>
                    <td><button type="button" className='button-put' onClick={put_nome}>Update</button></td>
                    <td><button type="button" className='button-delete' onClick={(e) => delete_nome(nome.id, nome.nome)}>Delete</button></td>
                </tr>
            
         ))}
         </tbody>
         </table>
        </center>
        </>
    )
}

export default App
