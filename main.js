'use strict'
var {BrowserWindow, app, ipcMain:ipc} = require('electron')
var {resolve} = require('path')
var {makeJoiner} = require('./util')
var url = require('url')

const joiner = makeJoiner('file:', __dirname);

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({width: 300, height: 550})
    mainWindow.loadURL(joiner('/app/index.html'))
    console.log('loaded')

        mainWindow.webContents.openDevTools()

    mainWindow.on('close', () => {
        mainWindow = null;
    })

};

app.on('ready', createWindow);

ipc.on('close-main-window', function() {
    app.quit();
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})
