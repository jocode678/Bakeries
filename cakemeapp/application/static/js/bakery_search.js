// NOT WORKING

const bakeries = [
  { bakery: "Maison Bertaux" },
  { bakery: "Bageriet" },
  { bakery: "Cutter & Squidge" },
];

// input form event listener
const searchInput = document.querySelector(".input", (e) => {
  // declare amd assign the value of the targets event to variable typed in the search bar by user
  let value = e.target.value;
  // check it exisits and input is larger than 0
  if (value && value.trim().length > 0) {
    // redefine valaue to exclude white space and change input to lower case
    value = value.trim().toLowerCase();
    // return results only if value of search is included in bakeries name
    // function to filter through our datta to inlude thh search input value
    searchInput.addEventListener("input", (e) => {
      let value = e.target.value;
      // check if input exisits and is large than 0
      if (value && value.trim().length > 0) {
        value = value.trim().toLowerCase();
        // returning the results of setList only if the value of search is included in the shop name
        setList(
          bakeries.filter((bakery) => {
            return bakery.name.includes(value);
          })
        );
      } else {
        // clear the list
        clearList();
      }
    });

    // clearing the search function
    const clearButton = document.getElementById("clear");
    clearButton.addEventListener("click", () => {
      // function to remove previous results goes here
      clearList();
    });

    // showing our results- appending to the webpage
    // creating and declaing a function called set lists
    // set list takes in a param of results
    function setList(results) {
      clearList();
      for (const bakery of results) {
        // creating li item for each result item
        const resultItem = document.createElement("li");
        //adding a cclass to each item of results
        resultItem.classList.add("result-item");
        // grabbing the name of the current loop point
        //and adding the  as the list items text
        const text = document.createTextNode(bakery.shopName);
        //appending the text to the result item
        resultItem.appendChild(text);
        // appending the result item to the list
        list.appendChild(resultItem);
      }
      // no results from set list function below
      if (results.length === 0) {
        noResults();
      }
    }

    // removing results from page, call list element and remove child as
    // all result items are children elements of list use a while loop
    // add to event listeners
    function clearList() {
      // looping through each child of search results list and removing them
      while (list.firstChild) {
        list.removeChild(list.firstChild);
      }
    }

    // no matches in search means no results
    // add to set list function
    function noResults() {
      // create an element for the err - a list item ("li")
      const error = document.createElement("li");
      // adding the class name 'error message' to error element
      error.classList.add("error-message");

      // element text
      const text = document.createTextNode(
        "No bakeries found with this name on our site"
      );
      // appending element text
      error.appendChild(text);
      // appending error to our ("li")
      list.appendChild(error);
    }
  }
});

// const BakerySearch = ({ bakeries = [] }) => {
//   return (
//     <>
//       {bakeries.map((data) => {
//         if (data) {
//           return (
//             <div key={data.id}>
//               <h1>{data.shop_name}</h1>
//             </div>
//           );
//         }
//         return null;
//       })}
//     </>
//   );
// };
