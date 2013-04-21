function saveEmailAddr() {
	//1. Get the address value
	address=document.getElementById('emailAddress').value;
	
	//2. Create a Request
	request=createRequest();
	
	//3. Set the url with parameters
	var url = '/saveAddress?Address='+escape(address)+'&Type=email'
	
	//4. Asynchronous GET request to the url
	request.open('GET', url, true);
	
	//5. Send without extras
	request.send(null);
}
function saveTextAddr() {
	//1. Get the address value
	address=document.getElementById('emailAddress').value;
	
	//2. Create a Request
	request=createRequest();
	
	//3. Set the url with parameters
	var url = '/saveAddress?Address='+escape(address)+'&Type=text'
	
	//4. Asynchronous GET request to the url
	request.open('GET', url, true);
	
	//5. Send without extras
	request.send(null);
	}