<template>
  <div class="hello">
    <h1 class="title">Task List</h1>
    <hr>

   <div class="columns">
  <div class="column is-one-third is-offset-one-third">
    <form v-on:submit.prevent="addTask">
      <h2 class="subtitle">Adicionar Tarefa</h2>

      <div class="field">
        <label class="label">Mensagem</label>
        <div class="control">
          <input class="input" type="text" v-model="message">
        </div>
      </div>

      <div class="field">
        <label class="label">Status</label>
        <div class="control">
          <div class="select">
            <select v-model="status">
              <option value="1">Pendente</option>
              <option value="2">Em andamento</option>
              <option value="3">Completa</option>
            </select>
          </div>
        </div>
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link">Criar</button>
        </div>
      </div>
    </form>
  </div>
</div>

    <hr>

    <div class="columns">
    <div class="column is-one-third">
    <h2 class="subtitle">Pendente</h2>
    <div class="todo">
      <div class="card" v-for="task in tasks" v-if="task.status == 1"> <!-- Loop through the tasks array, if status is 0 (to do) then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ task.message }} <!-- Print the task's message here -->
          </div>
        </div>

        <footer class="card-footer">
          <a class="card-footer-item" v-on:click="setStatus(task.id, 2)">Iniciar</a>
        </footer>
      </div>
    </div>
  </div>
    <div class="column is-one-third">
    <h2 class="subtitle">Em Andamento</h2>
    <div class="todo">
      <div class="card" v-for="task in tasks" v-if="task.status == 2">
        <div class="card-content">
          <div class="content">
            {{ task.message }}
          </div>
        </div>

        <footer class="card-footer">
          <a class="card-footer-item" v-on:click="setStatus(task.id,3)">Completa</a>
        </footer>
      </div>
    </div>
  </div>

  <div class="column is-one-third">
    <h2 class="subtitle">Completa</h2>

    <div class="done">
      <div class="card" v-for="task in tasks" v-if="task.status == 3">
        <div class="card-content">
          <div class="content">
            {{ task.message }}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
  </div>
</template>

<script>
  import axios from 'axios'
export default {
  name: 'TaskList',
  data () {
    return {
      tasks: [],
      message: '',
      status: 1
    }
  },
  mounted () {
    this.getTasks();
  },
  methods: {
    getTasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/tasks/',
        }).then(response => this.tasks = response.data);
    },
    addTask() {
  if (this.message) {
    axios({
      method:'post',
      url: 'http://127.0.0.1:8000/tasks/',
      data: { // Send message and status to the server
        message: this.message,
        status: this.status
      },
    }).then((response) => {
      let newTask = {'id': response.data.id, 'message': this.message, 'status': parseInt(this.status)};

      this.tasks.push(newTask);

      this.message = '';
      this.status = 1
    })
    .catch((error) => {
      console.log(error);
    });
  }
},
  setStatus(task_id, status) {
    let message = '';

    for (let i = 0; i < this.tasks.length; i++) {
    if (this.tasks[i].id === task_id) {
      this.tasks[i].status = status;
      message = this.tasks[i].message;

      break
    }
  }

  axios({
    method:'put',
    url: 'http://127.0.0.1:8000/tasks/' + task_id + '/',
    headers: {
      'Content-Type': 'application/json'
    },
    data: {
      message: message,
      status: status
    }
  })
},
  }

}
</script>

<style scoped>
.select, select {
  width: 100%;
}

.card {
  margin-bottom: 25px;
}

.done {
  opacity: 0.3;
}
</style>