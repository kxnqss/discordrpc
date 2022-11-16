
var applicationID = "1042078360861425705"
var details_content = "detail bro"
var largeimg = "piscio"
var largetext = "ur text"
var bt1_text = "ur button text"
var bt1_url = "https://www.google.com"

var rpc = require("discord-rpc")
const client = new rpc.Client({ transport: 'ipc' })
client.on('ready', () => {
	client.request('SET_ACTIVITY', {
		pid: process.pid,
		activity : {
			details : details_content,
			assets : {
				large_image : largeimg,
				large_text : largetext
			},
			buttons : [{label : bt1_text , url : bt1_url}]
		}
	})
})
client.login({ clientId : applicationID }).catch(console.error);
