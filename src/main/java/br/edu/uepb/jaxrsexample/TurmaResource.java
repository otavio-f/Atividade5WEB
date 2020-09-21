
package br.edu.uepb.jaxrsexample;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

// The Java class will be hosted at the URI path "/aluno"
@Path("/turmas")
public class TurmaResource {
	
	private static TurmaRepository repository = new TurmaRepository();
    
    @GET 
    // The Java method will produce content identified by the MIME Media
    // type "text/plain"
    @Produces("text/plain")
    public String getIt() {
        return "Got it!";
    }
}
