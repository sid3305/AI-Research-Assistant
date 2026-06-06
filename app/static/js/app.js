const sendBtn =
document.getElementById("sendBtn");

const uploadBtn =
document.getElementById("uploadBtn");

const scrapeBtn =
document.getElementById("scrapeBtn");

const chatMessages =
document.getElementById("chatMessages");

const questionInput =
document.getElementById("questionInput");

const typing =
document.getElementById("typing");

const statusDiv =
document.getElementById("status");


function addMessage(
    text,
    type
){

    const div =
    document.createElement("div");

    div.classList.add(
    `${type}-message`
);
    div.innerHTML =
    text.replace(
        /\n/g,
        "<br>"
    );

    chatMessages.appendChild(
        div
    );

    chatMessages.scrollTop =
    chatMessages.scrollHeight;

    const welcome = document.querySelector(
        ".welcome-card"
    );

    if(welcome){

        welcome.remove();
    }
}


async function askQuestion(){

    const question =
    questionInput.value.trim();

    if(!question){
        return;
    }

    addMessage(
        question,
        "user"
    );

    questionInput.value =
    "";

    typing.style.display =
    "block";

    try{

        const response =
        await fetch(
            "/ask",
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({
                    question:question
                })
            }
        );

        const data =
        await response.json();

        addMessage(
            data.answer ||
            data.error ||
            "Something went wrong.",
            "bot"
        );

    }catch(error){

        addMessage(
            "Failed to contact server.",
            "bot"
        );
    }

    typing.style.display =
    "none";
}


sendBtn.addEventListener(
    "click",
    askQuestion
);


questionInput.addEventListener(
    "keypress",
    function(event){

        if(
            event.key === "Enter"
        ){

            askQuestion();
        }
    }
);


uploadBtn.addEventListener(
    "click",
    async () => {

        const file =
        document
        .getElementById(
            "fileInput"
        )
        .files[0];

        if(!file){

            statusDiv.textContent =
            "Please select a file.";

            return;
        }

        const formData =
        new FormData();

        formData.append(
            "pdf_file",
            file
        );

        statusDiv.textContent =
        "Uploading document...";

        try{

            const response =
            await fetch(
                "/upload",
                {
                    method:"POST",
                    body:formData
                }
            );

            if(response.ok){

                statusDiv.textContent =
                `${file.name} loaded successfully`;

                addMessage(
                    `${file.name} uploaded successfully.`,
                    "bot"
                );

            }else{

                statusDiv.textContent =
                "Upload failed";
            }

        }catch(error){

            statusDiv.textContent =
            "Upload failed";
        }
    }
);


scrapeBtn.addEventListener(
    "click",
    async () => {

        const url =
        document
        .getElementById(
            "urlInput"
        )
        .value
        .trim();

        if(!url){

            statusDiv.textContent =
            "Please enter a URL.";

            return;
        }

        const formData =
        new FormData();

        formData.append(
            "url",
            url
        );

        statusDiv.textContent =
        "Loading website...";

        try{

            const response =
            await fetch(
                "/scrape",
                {
                    method:"POST",
                    body:formData
                }
            );

            const responseText =
            await response.text();

            console.log(
                responseText
            );

            if(response.ok){

                statusDiv.textContent =
                "Website loaded successfully";

                addMessage(
                    "Website content loaded successfully.",
                    "bot"
                );

            }else{

                statusDiv.textContent =
                responseText;

                addMessage(
                    responseText,
                    "bot"
                );
            }

        }catch(error){

            console.error(error);

            statusDiv.textContent =
            error.message;
        }
    }
);