
package br.edu.uepb.jaxrsexample;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.GenericEntity;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

// The Java class will be hosted at the URI path "/turma"
@Path("/turmas")
public class TurmaResource {
	
	private static TurmaRepository turmaRepository = new TurmaRepository();
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getTurmas() {
    	GenericEntity<List<Turma>> e = new GenericEntity<List<Turma>>(turmaRepository.getAll()){};
    	return Response.ok(e).build();
    }
    
    @POST
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createTurma(Turma aluno) {
    	turmaRepository.create(aluno);
    	return Response.status(Response.Status.CREATED)
    			.entity(aluno).build();
    }
    
    @GET
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getTurmaById(@PathParam("id") long id) {
    	Turma t = turmaRepository.getById(id);
    	if(t==null)
    		return Response.status(Response.Status.NOT_FOUND).build();
    	return Response.ok(t).build();
    }
    
    @PUT
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response editTurma(@PathParam("id") long id, Turma turma) {
    	Turma t = turmaRepository.getById(id);
    	if(t == null)
    		return Response.status(Response.Status.NOT_FOUND).build();
    	try {
    		turma.setId(id);
    		turmaRepository.edit(turma);
    		return Response.ok(turma).build();
    	} catch(Exception e) {
    		return Response
    				.status(Response.Status.INTERNAL_SERVER_ERROR)
    				.entity(e.getMessage()).build();
    	}
    }
    
    @DELETE
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response deleteTurma(@PathParam("id") long id) {
    	Turma t = turmaRepository.getById(id);
    	if(t == null)
    		return Response.status(Response.Status.NOT_FOUND).build();
    	try {
    		turmaRepository.delete(t);
    		return Response.noContent().build();
    	} catch(Exception e) {
    		return Response
    				.status(Response.Status.INTERNAL_SERVER_ERROR)
    				.entity(e.getMessage()).build();
    	}
    }
}
