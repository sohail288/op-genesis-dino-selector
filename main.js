'use strict'
var {BrowserWindow, app, ipcMain:ipc} = require('electron');
var {resolve} = require('path');
var {makeJoiner} = require('./util');

const joiner = makeJoiner('file://', resolve('app'));
console.log(resolve('app'), joiner('index.html'))

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({width: 300, height: 550, resizable: process.env.RESIZABLE == 1 ? true: false})  
    mainWindow.loadURL(joiner('index.html'))

    if (process.env.DEBUG == 1) {
        mainWindow.webContents.openDevTools()
    }

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
