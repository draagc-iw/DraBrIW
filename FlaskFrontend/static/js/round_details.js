function initAddDrink() {
    document.querySelectorAll('.order').forEach(element =>
        element.querySelector('.order__item-add')
            .addEventListener('click', () => App.util.toggle_child_visibility('.order__body', element)));

    document.querySelectorAll('.to-add')
        .forEach(element => element.addEventListener('click', (ev) => {
            const reqBody = {
                action: 'add',
                roundId: element.getAttribute('data-round-id'),
                drinkId: element.getAttribute('data-drink-id'),
                personId: element.getAttribute('data-person-id'),
            };

            App.req.post(location.href, reqBody)
                .then(() => location.reload())
                .catch((err) => alert(err));
        }));

}

function initAddPerson() {
    document.querySelector('.add-button').addEventListener('click', () => {
        if (document.querySelector('.order.not-added')) return;

        const content = document.querySelector('#new_order_template').content;
        const newNode = document.importNode(content, true);

        if (newNode.querySelector(".order__item-container").childElementCount < 1) {
            alert("No more people to to add");
            return;
        }
        newNode.querySelectorAll('.to-add')
            .forEach((element) => element.addEventListener('click', () =>
                App.req.post(location.href, {action: 'add', personId: element.getAttribute('data-add-id')})
                    .then(() => location.reload())
                    .catch((err) => alert(err))
            ));

        document.querySelector('.round-orders').appendChild(newNode);


    });
}

function initCloseRound() {
    document.querySelector('.close-round-button').addEventListener('click', () =>
        App.req.post(location.href, {action: 'close'})
            .then(() => location.href = '/app/rounds')
            .catch((err) => alert(err)));
}



initAddDrink();
initAddPerson();
initCloseRound();
