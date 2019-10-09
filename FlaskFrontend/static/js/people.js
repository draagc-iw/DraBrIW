function initNewPerson(){
    document.querySelector('.add-button').addEventListener('click', () =>
        App.util.toggle_child_visibility('.to-add'));

        document.querySelector('#form-person').addEventListener('submit', (ev) => {
        ev.preventDefault();
        const personFirstName = document.querySelector('#person-first-name').value;
        const personLastName = document.querySelector('#person-last-name').value;
        if (personFirstName.length < 1 || personLastName.length < 1) alert('Person name cannot be empty');
        else {
            App.req.post(location.href, {personFirstName, personLastName})
                .then(() => location.reload())
                .catch((err) => alert(err))
        }
    });

}

initNewPerson();