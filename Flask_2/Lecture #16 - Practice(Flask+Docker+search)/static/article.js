fetch("/api/articles")
    .then(response => response.json())
    .then(function (response) {
        var post_area = document.getElementById("post_area");
        var list = document.createElement("ul");
        list.classList.add("post-list");

        for (let el of response) {
            var listItem = document.createElement("li");
            listItem.classList.add("post-item");

            fetch(`/api/post-author/${el.user_id}`)
                .then(response => response.json())
                .then(function (author) {
                    var postContainer = document.createElement("div");
                    postContainer.classList.add("post-container");

                    var title = document.createElement("h5");
                    title.classList.add("post-title");
                    title.textContent = el.post_header;

                    var subtitle = document.createElement("h6");
                    subtitle.classList.add("post-date");
                    subtitle.textContent = el.post_datetime;

                    var text = document.createElement("p");
                    text.classList.add("post-text");
                    text.textContent = el.post_text;

                    var authorName = document.createElement("h6");
                    authorName.classList.add("post-author");
                    authorName.textContent = author.first_name + " " + author.last_name;

                    postContainer.appendChild(title);
                    postContainer.appendChild(subtitle);
                    postContainer.appendChild(text);
                    postContainer.appendChild(authorName);

                    if (author.logg_status === true) {
                        var buttonGroup = document.createElement("div");
                        buttonGroup.classList.add("button-group");

                        var editButton = document.createElement("a");
                        editButton.href = `/post/${el.post_id}/edit`;
                        editButton.classList.add("btn", "btn-primary", "edit-button");
                        editButton.textContent = "Edit";

                        var deleteButton = document.createElement("a");
                        deleteButton.href = `/post/${el.post_id}/delete`;
                        deleteButton.classList.add("btn", "btn-primary", "delete-button");
                        deleteButton.textContent = "Delete";

                        buttonGroup.appendChild(editButton);
                        buttonGroup.appendChild(deleteButton);
                        
                        postContainer.appendChild(buttonGroup);
                    }

                    list.appendChild(postContainer);
                })
                .catch(error => console.log(error));
        }

        post_area.appendChild(list);
    })
    .catch(error => console.log(error));
