import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import './App.css'
import './scss/main.scss';
import Navbar from './components/header/Navbar.jsx'
import Footer from './components/footer/Footer.jsx'
import Home from './pages/1.home/Home.jsx'
import Contact from './pages/2.contact/Contact.jsx'
import About from './pages/3.about/About.jsx'
function App() {


  return (
      <div>

      <Router>
        <Navbar></Navbar>
        <Routes>
          <Route exact path={'/'}element={<Home/>}/>
          <Route exact path={'/contact'} element={<Contact/>}/>
          <Route exact path={'/about'} element={<About/>}/>
        </Routes>
        <Footer></Footer>
      </Router>
    </div>

  )
}

export default App
