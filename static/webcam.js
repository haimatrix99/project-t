let video, canvas, snapshotButton, datetimeDisplay, stream = null;

function initializeElements() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    snapshotButton = document.getElementById('snapshotButton');
    datetimeDisplay = document.getElementById('datetimeDisplay');
    return true;
}


async function startWebcam() {
    if (!initializeElements()) return;

    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        video.srcObject = stream;
    } catch(err) {
        console.error("Error accessing the webcam", err);
    }
}

function stopWebcam() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
    }
}

function formatDate(date) {
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');  // Months are 0-indexed
    const year = date.getFullYear();
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    return `${day}/${month}/${year}, ${hours}:${minutes}:${seconds}`;
}

async function takeSnapshot() {
    if (!initializeElements()) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    let data = canvas.toDataURL('image/jpeg');
    
    let now = new Date();
    datetimeDisplay.textContent = `Snapshot taken on: ${formatDate(now)}`;

    let response = await fetch('/process_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({image: data}),
    });

    console.log(await response.json());
    timeSnapshot.setAttribute('data-content', Date.now());
    timeSnapshot.style.display = 'block';
}

function checkIn() {
    console.log("Check in button clicked");
}

function checkOut() {
    console.log("Check out button clicked");
}

window.addEventListener('load', startWebcam);
window.addEventListener('unload', stopWebcam);