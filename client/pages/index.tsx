import React, {useEffect, useState} from "react";

function index() {

  const [message, setMessage] = useState("Loading"); 

  useEffect(() => {
    fetch("http://localhost:8080/api/home").then(
      repsonse => repsonse.json()).then(
        data => {
          //message will be intially set to loading 
          //once data is sent
          // message = data.message

          setMessage(data.message);
        });
  }, []);


  return <div>{message}</div>;
}

export default index;