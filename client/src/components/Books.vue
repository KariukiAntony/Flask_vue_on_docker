<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="text-center">Books</h1>
        <hr />
        <br /><br />
        <alert :message="message" v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal"
        >
          Add Book
        </button>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="toggleEditBookModal(book)"
                  >
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteBook(book)">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- add new book model  -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new book</h5>
            <button
              style="margin-left: 297px"
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddBookModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookTitle"
                  v-model="addBookForm.title"
                  placeholder="Enter title"
                />
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addBookForm.author"
                  placeholder="Enter author"
                />
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addBookRead"
                  v-model="addBookForm.read"
                />
                <label class="form-check-label" for="addBookRead">Read?</label>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset"
                >
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>

    <!-- edit book modal -->
    <div
      ref="editBookModal"
      class="modal fade"
      :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update</h5>
            <button
              style="margin-left: 387px"
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleEditBookModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="editBookTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookTitle"
                  v-model="editBookForm.title"
                  placeholder="Enter title"
                />
              </div>
              <div class="mb-3">
                <label for="editBookAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookAuthor"
                  v-model="editBookForm.author"
                  placeholder="Enter author"
                />
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="editBookRead"
                  v-model="editBookForm.read"
                />
                <label class="form-check-label" for="editBookRead">Read?</label>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleEditSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleEditCancel"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeEditBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert.vue";
let BASE_URL = "http://127.0.0.1:/api"
let DEV_BASE_URL = "http://127.0.0.1:5000/api" //* NB, use this url when you are not using nginx to proxy your requests
let SECONDS = 1600

export default {
  name: "Books",
  components: {
    alert: Alert,
  },

  data() {
    return {
      activeAddBookModal: false,
      activeEditBookModal: false,
      addBookForm: {
        title: "",
        author: "",
        read: [],
      },
      editBookForm: {
        id: "",
        title: "",
        author: "",
        read: [],
      },
      books: [],
      message: "",
      showMessage: false,
    };
  },
  methods: {
    hide_message(seconds=1000){
      setTimeout(() => {
        this.showMessage = false;
      }, seconds);
    },
    addBook(payload) {
      const path = `${BASE_URL}/books`;
      axios
        .post(path, payload)
        .then((resp) => {
          this.getBooks();
          this.message = resp.data.message;
          console.log(resp.data.message)
          this.showMessage = true;
          this.hide_message(SECONDS)
        })
        .catch((error) => {
          this.getBooks();
        });
    },
    getBooks() {
      const path = `${BASE_URL}/books`;
      axios
        .get(path)
        .then((resp) => {
          this.books = resp.data.books;
        })
        .catch((error) => {
          console.error(error.message);
        });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddBookModal();
      let read = false;
      if (this.addBookForm.read[0]) {
        read = true;
      }
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read,
      };
      this.addBook(payload);
      this.initForm();
    },
    initForm() {
      this.addBookForm.title = "";
      this.addBookForm.author = "";
      this.addBookForm.read = [];
      this.editBookForm.id = "",
      this.editBookForm.title = "",
      this.editBookForm.author = "",
      this.editBookForm.read = []
    },
    toggleAddBookModal() {
      const body = document.querySelector("body");
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add("model-open");
      } else {
        body.classList.remove("modal-open");
      }
    },

    toggleEditBookModal(book){
        if(book){
            this.editBookForm = book;
        }
        const body = document.querySelector("body")
        this.activeEditBookModal = !this.activeEditBookModal;
        if(this.activeEditBookModal){
            body.classList.add("modal-open");
        }else{
            body.classList.remove("modal-open");
        }
    },
    handleEditSubmit(){
        this.toggleEditBookModal(null);
        let read = false;
        if(this.editBookForm.read) read = true ;
        const payload = {
            title: this.editBookForm.title,
            author: this.editBookForm.author,
            read
        };
        this.updateBook(payload, this.editBookForm.id)
    },
    updateBook(payload, bookID){
        const path = `${BASE_URL}/books/${bookID}`
        axios.put(path, payload)
        .then((resp)=> {
            this.getBooks();
            this.message = resp.data.message;
            this.showMessage = true
            this.hide_message(SECONDS)
        })
        .catch((error) => {
            console.error(error)
            this.getBooks()
        })
    },
    handleEditCancel(){
        this.toggleEditBookModal(null)
        this.initForm();
        this.getBooks();
    },
    handleDeleteBook(book){
        this.removeBook(book.id)
    },
    removeBook(bookID){
        const path = `${BASE_URL}/books/${bookID}`
        axios.delete(path)
        .then((resp) => {
            this.getBooks()
            console.log(`delete message: ${resp.data.message}`)
            this.message = resp.data.message;
            this.showMessage = true
            this.hide_message(SECONDS)
        })
        .catch((error) => {
            console.error(error.message)
            this.getBooks()
        });
    },
  },
  created() {
    this.getBooks();
  },

};
</script>
