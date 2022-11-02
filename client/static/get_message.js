alert("Server loading...");

// Connect to MongoDB

const {MongoClient} = require('mongodb');
async function main() {
	const uri = "";
    const client = new MongoClient(uri);
    await client.connect();
    await listDatabases(client);
    try {
        await client.connect();
        await listDatabases(client);
    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
    }
}

main().catch(console.error);

async function listDatabases(client){
    databasesList = await client.db().admin().listDatabases();
    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));
}