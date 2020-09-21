
package br.edu.uepb.jaxrsexample;

import com.sun.jersey.api.container.grizzly2.GrizzlyServerFactory;
import com.sun.jersey.api.core.PackagesResourceConfig;
import com.sun.jersey.api.core.ResourceConfig;
import org.glassfish.grizzly.http.server.HttpServer;

import javax.ws.rs.core.UriBuilder;
import java.io.IOException;
import java.net.URI;


public class Main {

    public static final URI BASE_URI = URI.create("http://localhost:8080/api/");
    
    protected static HttpServer startServer() throws IOException {
        ResourceConfig resourceConfig = new PackagesResourceConfig("br.edu.uepb.jaxrsexample");

        System.out.println("Starting grizzly2...");
        return GrizzlyServerFactory.createHttpServer(BASE_URI, resourceConfig);
    }
    
    public static void main(String[] args) throws IOException {
        // Grizzly 2 initialization
        HttpServer httpServer = startServer();
        System.out.println(String.format("Jersey app started with WADL available at "
                + "%sapplication.wadl\nHit enter to stop it...",
                BASE_URI));
        System.in.read();
        httpServer.stop();
    }    
}
