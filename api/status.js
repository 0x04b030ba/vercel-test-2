// api/status.js

module.exports = async (req, res) => {
    // Simulated bot status, could check an actual API in a real scenario
    res.status(200).send("Bot is running!");
};
