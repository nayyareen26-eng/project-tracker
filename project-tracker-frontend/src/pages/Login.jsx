import { useNavigate } from "react-router-dom";
import { useState } from "react";
import {
  TextField,
  Button,
  Box,
  Typography,
  Paper
} from "@mui/material";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/login",
        {
          email: email,
          password: password
        }
      );

      console.log(res.data); // backend response

      // save user info
      localStorage.setItem("user", JSON.stringify(res.data));
      
      navigate("/departments");
      
      alert("Login Successful");
      // later: navigate to dashboard

    } catch (err) {
      setError("Invalid email or password");
    }
  };

  return (
    <Box
      sx={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#F5EDED"
      }}
    >
      <Paper sx={{ padding: 4, width: 350 }}>
        <Typography 
        variant="h5" 
        align="center" 
        mb={2}
        sx={{
          color:"#6482AD",
          fontWeight: "bold"
        }}
        >
          Login
        </Typography>

        <TextField
          label="Email"
          fullWidth
          margin="normal"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <TextField
          label="Password"
          type="password"
          fullWidth
          margin="normal"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        {error && (
          <Typography color="error" variant="body2">
            {error}
          </Typography>
        )}

        <Button
          variant="contained"
          fullWidth
          sx={{
            backgroundColor: "#7FA1C3",
            "&:hover": {
              backgroundColor: "#E2DAD6"
  }
}}
          onClick={handleLogin}
        >
          Login
        </Button>
      </Paper>
    </Box>
  );
};

export default Login;
