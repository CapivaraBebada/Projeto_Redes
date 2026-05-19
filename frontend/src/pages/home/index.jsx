import { useState } from "react";
import "./style.css";

function Home() {
  return (
    <div className="container">
      <div>
        <section className="cadastro">
          <label>Digite seu nome</label>
          <input placeholder="ex: maria"></input>
          <label>Digite seu nome de usuário</label>
          <input placeholder="ex: maria123"></input>
          <label>Crie uma senha</label>
          <input placeholder="digite sua senha"></input>
          <button>cadastrar</button>
        </section>
      </div>
    </div>
  );
}

export default Home;
