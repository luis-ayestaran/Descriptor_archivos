package com.sgbd.dao;

import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Descriptor {
	static File archivo;
    ArrayList<String> datos= new ArrayList<String>();
    ArrayList<String> nombres=new ArrayList<String>();
    ArrayList<String> sueldos=new ArrayList<String>();
    
    public Descriptor() {
    	URL url = getClass().getResource("/files/EMPLOYEES.txt");
    	archivo = new File(url.getPath());
    }
    public boolean columna(String columna) throws IOException 
    {    
        DataInputStream file = new DataInputStream(new FileInputStream(archivo));
        String cadena;
        String texto;
        int sizetoken;
        boolean verdad = false;
        cadena = file.readLine();
        StringTokenizer sr = new StringTokenizer(cadena,",");
        sizetoken = sr.countTokens();
        for(int i = 0 ;i < sizetoken;i++)
        {
            texto = sr.nextToken();
            if(texto.equals(columna))
            {
                verdad = true;
                break;
            }
        }
        return verdad;
    }
   public String seleccion(String columna,int down, int up)throws IOException
   {
        DataInputStream file = new DataInputStream(new FileInputStream(archivo));//archivo
        StringBuilder sb = new StringBuilder();
        String cadena;
        String subcadena;
        String texto;
        String temp;
        int sizetoken;
        int inicio=0;
        int fin=0;
        cadena = file.readLine();//leemos el decriptor de archivo
        StringTokenizer sr = new StringTokenizer(cadena,",");//subdibidimos la linea leida
        sizetoken = sr.countTokens();//obtenemos el numero de subcadenas
        for(int i = 0 ;i < sizetoken;i++)//rrecorremos las subcadena 
        {
            texto = sr.nextToken();
            if(texto.equals(columna))//localizamos las columna deseada
            {
                inicio = Integer.parseInt(sr.nextToken());//obtenemos el taÃ±ano del tato
                fin = Integer.parseInt(sr.nextToken());//el fin del dato
                break;//salimos cunado cobtenemos los datos
            }
        }   
        while((cadena = file.readLine()) != null)//accedemos para leer todas las linesas
        {
            subcadena = cadena.substring(inicio, fin) ;//llemos la linea y no dirigimos solo a la posision del dato
            temp="";
            for(int i = 0 ; i < subcadena.length();i++)//proceso para convertirlo de strong a int
            {
                if(subcadena.charAt(i)!= ' ')
                {
                    temp = temp +  subcadena.charAt(i);   
                }    
            }
                if(Integer.parseInt(temp) >= down && Integer.parseInt(temp) <= up )//hacemos la seleccion de los datos
                {
                    datos.add(cadena);//se alamcenan los datos que cumplan en un arraylist
                    sb.append(cadena + "\n");
                }
        }
        return sb.toString();
   }
   public String all()throws IOException//esta funcion muestra todos los datos del archivo
   {
       DataInputStream file = new DataInputStream(new FileInputStream(archivo));
       StringBuilder sb = new StringBuilder();
       String fila;
       fila = file.readLine();
       while((fila = file.readLine())!= null)
       {
    	   sb.append(fila + "\n");
       }
       return sb.toString();
   }
   public String proyeccion(String campo1, String campo2) throws IOException{
	   StringBuilder sb = new StringBuilder();
       if(columna(campo1) && columna(campo2)==true){
           String linea,sueldo=null, nombre = null;
        for(int i=0;i<datos.size();i++)//leemos los resultados obtenidos
        {
            linea=datos.get(i);
            StringTokenizer st = new StringTokenizer(linea);// subdividimos la cadena en sub cadenas 
            for(int j = 2; j > 0; j--)// hasel espacio 2 que es el del nombre
            {
                nombre = st.nextToken();// alamacenamos solo nombre
            }
            nombres.add(nombre);    // se pasa a la estructura de nombres
            for(int j=8;j>2;j--){
                sueldo=st.nextToken();// alamacenamos solo sueldo
            }
            String temp="";
            for(int j = 0 ; j < sueldo.length();j++)//proceso para convertirlo de strong a int
            {
                if((sueldo.charAt(j)>='0' && sueldo.charAt(j)<='9'))
                {
                    temp = temp +  sueldo.charAt(j);   
                }    
            }
            sueldos.add(temp);// se pasa a la estructura de sueldos
            sb.append(nombre + "\t" + temp + "\n");
         }
       }
       return sb.toString();
   }
     public static void main(String[] args) 
     {
         Descriptor des = new Descriptor();
         try
         {
           String objeto = "salary";
           if(des.columna(objeto))
           {
        	   System.out.println(des.all());
               System.out.println(des.seleccion(objeto, 4000, 6000));
               System.out.println(des.proyeccion("first_name","salary"));
           }
           else
           {
               System.out.println("ERROR NO EXISTE EL OBJETO " + objeto);
           }
           
         }
         catch(IOException e)
         {
            System.out.println("HA OCURRIDO UN ERROR"); 
         }
     }
}
