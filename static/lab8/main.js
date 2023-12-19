function fillCourseList() {
    fetch('/lab8/api/courses/')
    .then(function(data) {
        return data.json();
    })
    .then(function (courses) {
        let tbody = document.getElementById('course-list');
        tbody.innerHTML='';
        for(let i = 0; i<courses.length; i++) {
            let tr = document.createElement('tr');

            let tdName = document.createElement('td');
            tdName.innerText = courses[i].name;

            let tdVideos = document.createElement('td');
            tdVideos.innerText = courses[i].videos;

            let tdPrice = document.createElement('td');
            tdPrice.innerText = courses[i].price || 'бесплатно';

            let tdCreatedDate = document.createElement('td');
            tdCreatedDate.innerText = courses[i].created_date;

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                editCourse(i, courses[i]);
            };

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteCourse(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdCreatedDate);
            tr.append(tdActions);

            tbody.append(tr);
        }
    });
}