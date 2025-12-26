import { BrowserRouter , Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Departments from "./pages/Department";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/departments" element={<Departments />}/>

        </Routes>
      </BrowserRouter>
  );
}

export default App;