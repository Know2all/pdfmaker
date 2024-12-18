**Async Django Pdf Converter (From Html to Pdf )**

This API allows users to convert any HTML page (specified by a URL) into a PDF document encoded in base64 format. Built using Django with asynchronous handling, it ensures efficient resource management and responsiveness, even for concurrent requests.

**Getting Started**

**1. Setup:** Ensure you have Django, pyppeteer, and asyncio installed in your environment by using follow command .

    > pip install django pyppeteer asyncio

**2. Endpoints:**

**Test Endpoint:** GET /test/

Returns a JSON response to confirm the server and async clock function are operational. It returns an example response like this .

**Example Response :**
>{
    "status": "ok",
    "alarm": "alarmed"
}

**3. Generate PDF Endpoint: POST /generate_pdf_from_url**/

It converts the HTML content of a provided URL into a base64-encoded PDF.
**Parameters:** Requires a url parameter in the POST body.

Example
> {
    "url": "https://example.com"
}

**Response:**

On success, returns a base64-encoded PDF file.
On error, returns an error message

**Successful Response Example:**
>{
    "pdf": "JVBERi0xLjQKJcfs... (base64 encoded PDF)"
}

**Error Response Example :**
>{
    "error": "No URL provided"
}

**Usage:**

To test the functionality, send a POST request to /generate_pdf_from_url/ with the target URL.
This endpoint will return a JSON response containing the base64-encoded PDF, which can be decoded and saved as a .pdf file on the client side.

**Notes:**

This API is asynchronous, allowing multiple requests to be handled concurrently.
It requires an internet connection for accessing the specified URLs and converting their HTML content.

