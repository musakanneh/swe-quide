class Book {
    constructor(title, author, isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }
};

class UI { 
    addBookToList(book) {
        const list = document.getElementById('book-list');
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${book.title}</td>
        <td>${book.author}</td>
        <td>${book.isbin}</td>
        <td><a href="" class="delete">X</a></td>
        `
        list.appendChild(row);
    };

    showAlert(message, className) {
        const div = document.createElement('div');
        div.className = `alert${className}`;
        div.appendChild(document.createTextNode(message));

        const container = document.querySelector('.container');
        const form = document.querySelector('#book-form');
        container.insertBefore(div, form);

        setTimeout(function () {
            document.querySelector('.alert').remove();
        }, 3000);
    };

    deleteBook(target) {
        if (target.className == 'delete') {
            target.parentEelement.parentEelement.remove();
        }
    }

    clearInputFields() {
        document.getElementById('title').value = '';
        document.getElementById('author').value = '';
        document.getElementById('isbin').value = '';
    }
};

document.getElementById('book-form').addEventListener('submit', function (e) {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const isbin = document.getElementById('isbin').value;

    const book = new Book(title, author, isbin);
    const ui = new UI();

    if (title === '' || author === '' || isbin === '') {
        ui.showAlert('Please fill in the fields', 'error');
    } else {
        ui.addBookToList(book);
        ui.showAlert('Book added to list', 'success');
        ui.clearInputFields();
    }
    e.preventDefault();
});

document.getElementById('book-list').addEventListener('click', function (e) {
    const ui = new UI();
    ui.deleteBook(e.target);
    ui.showAlert('Book Removed!', 'success');
    e.preventDefault();
}); 
