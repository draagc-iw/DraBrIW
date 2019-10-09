function initNewRound() {
    const elAdd = document.querySelector('.list-add');
    if (elAdd) {
        elAdd.addEventListener('click', () =>
            App.util.toggle_child_visibility('.list-add'));

        elAdd.querySelectorAll('.to-add')
            .forEach((element) => element.addEventListener('click', () => {
                const path = '/app/rounds';
                const initiatorId = element.getAttribute('data-add-id');

                App.req.post(path, {id: initiatorId})
                    .then((response) => location.reload())
                    .catch((err) => alert(err));
            }));
    }

}

function initAddDrink() {
    document.querySelectorAll('.order').forEach(element =>
        element.querySelector('.order__item-add')
            .addEventListener('click', () => App.util.toggle_child_visibility('.order__body', element)));

    document.querySelectorAll('.to-add')
        .forEach(element => element.addEventListener('click', (ev) => {
            const reqBody = {
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

        if(newNode.querySelector(".order__item-container").childElementCount < 1) {
            alert("No more people to to add");
            return;
        }
        newNode.querySelectorAll('.to-add')
            .forEach((element) => element.addEventListener('click', () =>
                App.req.post(location.href, {personId: element.getAttribute('data-add-id')})
                    .then(() => location.reload())
                    .catch((err) => alert(err))
            ));

        document.querySelector('.round-orders').appendChild(newNode);


    });
}

initNewRound();
initAddDrink();
initAddPerson();