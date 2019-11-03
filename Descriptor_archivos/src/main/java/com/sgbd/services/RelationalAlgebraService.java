package com.sgbd.services;

import java.io.IOException;

import com.sgbd.dao.Descriptor;

public class RelationalAlgebraService {
	Descriptor des;
	
	public RelationalAlgebraService() {
		des = new Descriptor();
        
	}
	
	public String mostrarTabla(/*String tableName*/) {
		String result = "";
		try
        {
			result = des.all();
        }
        catch(IOException e)
        {
            
        }
		return result;
	}
	
	public String mostrarSelectQuery(Integer from, Integer to) {
		return "SELECT FIRST_NAME,SALARY\nFROM EMPLOYEES\nWHERE SALARY BETWEEN " + String.valueOf(from) +  " AND " + String.valueOf(to);
	}
	
	public String select(String column, Integer from, Integer to) throws IOException {
		String result = "";
		try
        {
          if(des.columna(column))
          {
              result = des.seleccion(column, from, to);
          }
          else
          {
              result = "Error, no existe la columna " + column;
          }
          
        }
        catch(IOException e)
        {
            
        }
		return result;
	}
	
	public String project() throws IOException {
		String result = "";
		try
        {
			result = des.proyeccion("first_name","salary");
          
        }
        catch(IOException e)
        {
            
        }
		return result;
	}
	
}
