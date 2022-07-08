$('#search-books-results-display').css("display", "none");
$('#search-clients-results-display').css("display", "none")
jQuery(window).on('load', function(){
    $('#search-books-submit').click(function(e){
        const searchBook = $('#sf').val();

        if(searchBook.length>0){
            fetch("/", {
                body: JSON.stringify({ searchBooks: searchBook }),
                method: "POST",
            })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data", data);
                    $('#search-books-results-hide').css("display", "none");
                    $('#search-books-results-display').html("");
                    $('#search-books-results-display').css("display", "flex");

                    if(data.length===0){
                        $('#search-books-results-display').html("No results found");
                    } else {
                        
                        data.forEach((item) => {
                            $('#search-books-results-display').append(`<div id="search_books_data" class="books-result-container"><a href="#"><h3>"${item.title}" - ${item.author}</h3></a></div>`);
                        });
                    }
                });
        }
    });

    $('#search-clients-submit').click(function(){
        const searchClient = $('#search-clients-bar').val();

        if(searchClient.length>0){
            fetch("", {
                body: JSON.stringify({searchClients: searchClient}),
                method: "POST",
            })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data", data)
                    $('#search-clients-results-hide').css("display", "none");
                    $('#search-clients-results-display').html("");
                    $('#search-clients-results-display').css("display", "flex");

                    if(data.length===0){
                        $("#search-clients-results-display").html("No results found")
                    } else {
                        data.forEach((item) => {
                            $('#search-clients-results-display').append(`<div id="search_clients_data" class="clients-result-container"><a href="#"><h3>"${item.name}" - ${item.phone}</h3></a></div>`);
                        });
                    }
                })

        }
    });
});
