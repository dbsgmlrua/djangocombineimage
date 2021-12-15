import './App.css';
import { Container, Card, CardGroup, ListGroup, ListGroupItem, Button, Row, Image } from "react-bootstrap";
function App() {
  function createElements(n){
      var elements = [];
      for(var i =0; i < n; i++){
        let uri = "http://localhost:8000/png/image/" + (i % 7 + 1) + "/" + parseInt(i / 7 % 7 + 1)  + "/"+ parseInt(i / 7 / 7 % 7 + 1)
          elements.push(
              <div className="col-md-3 p-3" key={i}>
                  <Card border="dark">
                      <Card.Img variant="top" src={uri} height="286" />
                      <Card.Body>
                          <Card.Title href="#">{"item.name"}</Card.Title>
                          <Card.Text align="right">asjaskfakdgjkljgsla</Card.Text>
                      </Card.Body>
                      <ListGroup className="list-group-flush">
                          <ListGroupItem><Button variant="primary">Buy</Button></ListGroupItem>
                      </ListGroup>
                  </Card>
              </div>
          );
      }
      return elements;
  }


  function gomElements(){
    var elements = [];
    for(var i =0; i < 7; i++){
      for(var a=0;a<1;a++){
        for(var b=0;b<=8;b++){
          for(var c=0;c<=6;c++){
            for(var d=0;d<=14;d++){
              for(var e=0;e<=9;e++){
                let uri = "http://localhost:8000/png/imagenew/" + i + "/" + a  + "/"+ b + "/"+ c + "/"+ d + "/"+ e;
                elements.push(
                  <div className="col-md-3 p-3" key={i}>
                      <Card border="dark">
                          <Card.Img variant="top" src={uri} height="286" />
                          <Card.Body>
                              <Card.Title href="#">{"item.name"}</Card.Title>
                              <Card.Text align="right">asjaskfakdgjkljgsla</Card.Text>
                          </Card.Body>
                          <ListGroup className="list-group-flush">
                              <ListGroupItem><Button variant="primary">Buy</Button></ListGroupItem>
                          </ListGroup>
                      </Card>
                  </div>
                );
              }
            }
          }
        }
      }
    }
    return elements;
}
  return (
    <div className="App">
      <Container>
        <CardGroup>
          {gomElements()}
        </CardGroup>
      </Container>
    </div>
  );
}

export default App;
