const listDeSorts = fetch("Data/sorts.json")
    .then(response => response.json())
    .then(listeDeSorts => {
        console.log(listDeSorts)
        for (const sort of listeDeSorts) {
    console.log(sort.name)
};
    });


