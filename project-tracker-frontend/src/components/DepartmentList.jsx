import React, { useEffect, useState } from "react";
import api from "../services/api";
import {
  Card,
  CardContent,
  Typography
} from "@mui/material";

function DepartmentList() {
  const [departments, setDepartments] = useState([]);

  useEffect(() => {
    api.get("/api/departments")
      .then((res) => {
        setDepartments(res.data);
      })
      .catch((err) => {
        console.error("Error fetching departments", err);
      });
  }, []);

  return (
    <>

      {departments.map((dept) => (
        <Card key={dept.department_id} sx={{ mb: 2 }}>
          <CardContent>
            <Typography variant="h6">
              {dept.department_name}
            </Typography>

            <Typography color="#6482AD">
              Type: {dept.department_type}
            </Typography>
          </CardContent>
        </Card>
      ))}
    </>
  );
}

export default DepartmentList;
