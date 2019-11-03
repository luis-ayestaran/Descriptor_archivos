package com.sgbd.views.controllers;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

import com.sgbd.services.RelationalAlgebraService;

import javafx.scene.control.TextArea;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;

public class MainScreenController implements Initializable {
	
	@FXML TextArea txtOperation;
	@FXML TextArea txtResults;
	
	RelationalAlgebraService service;
	
	public void initialize(URL location, ResourceBundle resources) {
		service = new RelationalAlgebraService();
	}
	
	
	
	@FXML
	protected void writeSelect() {
		txtOperation.appendText("SELECT FIRST_NAME,SALARY\n");
	}
	
	@FXML
	protected void writeFrom() {
		txtOperation.appendText("FROM EMPLOYEES\n");
	}
	
	// ------------------------ IMPRIMIR TABLA -------------------------------//
	public void printTable(String tabla) {
		txtResults.appendText("TABLA EMPLEADOS \n\n" + tabla + "\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n");
	}
	
	
	// ------------------------ SELECCION -------------------------------//
	
	@FXML
	protected void select() { //Método llamado desde el botón
		makeSelect();
	}
	
	public void makeSelect() { //Realizamos el select
		try {
			Integer from = 4000; //Variables con valores arbitrarios (por ahora)
			Integer to = 6000; //que definen el intervalo de nuestro SELECT
			ArrayList<String> projectCols = new ArrayList<String>(); //y las columnas a proyectar (PENDIENTE POR IMPLEMENTAR CORRECTAMENTE)
		
			projectCols.add("first_name");	//(PENDIENTE)
			projectCols.add("salary");		//(PENDIENTE)
			
			printSelect(service.mostrarSelectQuery(from, to)); //Mostramos el SELECT realizado
			printTable(service.mostrarTabla()); //Mostramos toda la tabla
			printResultSelect(service.select("salary", from, to)); //Imprimimos el resultado de la query
			
			if(projectCols.size() != 0) {
				makeProject();
			}
			
			service = new RelationalAlgebraService();
		} catch(IOException e) {
			txtResults.setText("No se encontró la base de datos.");
		}
	}
	
	private void printSelect(String select) {
		txtOperation.setText(select);
	}
	
	private void printResultSelect(String seleccion) {
		txtResults.appendText("SELECCIÓN \n\n" + seleccion + "\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n");
	}
	
	// ------------------------ PROYECCION -------------------------------//
	
		@FXML
		protected void project() { //Método llamado desde el botón
			makeProject();
		}
		
		public void makeProject() { //Realizamos el select
			try {
				printResultProject(service.project()); //Imprimimos el resultado de la query
			} catch(IOException e) {
				txtResults.appendText("No se encontró la base de datos.");
			}
		}
		
		private void printProject(String project) {
			txtOperation.appendText(project);
		}
		
		private void printResultProject(String proyeccion) {
			txtResults.appendText("PROYECCIÓN \n\n" + proyeccion + "\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n");
		}
}
