package com.sgbd.app;

import com.sgbd.views.MainScreen;

public class App{
	
    public static void main( String[] args ) {
        App app = new App();
        app.initialise(args);
    }
    
    private void initialise(String[] args) {
    	new MainScreen().launchView(args);
    }
}
