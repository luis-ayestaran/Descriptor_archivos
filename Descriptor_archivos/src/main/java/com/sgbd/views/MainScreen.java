package com.sgbd.views;

import java.io.IOException;

import com.sgbd.views.controllers.MainScreenController;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Rectangle2D;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.Parent;
import javafx.stage.Screen;
import javafx.stage.Stage;

public class MainScreen extends Application {
	
	private static Stage stage;
	private static MainScreenController mainScreenController;
	
	public MainScreen() {}
	
	public void launchView(String args[]) {
		launch(MainScreen.class,args);
	}
	
	public static Stage getStage() {
		return stage;
	}
	
	public static void setStage(Stage s) {
		stage = s;
	}
	
	public static MainScreenController getMainScreenController() {
		return mainScreenController;
	}
	
	public static void setMainScreenController(MainScreenController controller) {
		mainScreenController = controller;
	}
	
	//@Override
	public void loadView() {//start(Stage primaryStage) {
		
	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		setStage(primaryStage);
		FXMLLoader loader = null;
		Parent root = null;
		try {
			loader = new FXMLLoader(getClass().getResource("/fxml/mainScreen.fxml"));
			root = loader.load();
		} catch(IOException e) {
			e.printStackTrace();
		}
		MainScreenController controller = (MainScreenController) loader.getController();
		setMainScreenController(controller);
		
		Scene scene = new Scene(root, 1000, 600);
		getStage().setScene(scene);
		getStage().setTitle("Descriptor de archivos");
		
		Rectangle2D primaryScreenBounds = Screen.getPrimary().getVisualBounds();

	    //set Stage boundaries to visible main screen bounds
	    getStage().setX(primaryScreenBounds.getMinX());
	    getStage().setY(primaryScreenBounds.getMinY());
	    getStage().setWidth(primaryScreenBounds.getWidth());
	    getStage().setHeight(primaryScreenBounds.getHeight());
		
		Image icon = new Image("/stylesheets/images/icon.png");
		getStage().getIcons().add(icon);
		getStage().setMaximized(true);
		getStage().show();
		
	}
	
	
}
