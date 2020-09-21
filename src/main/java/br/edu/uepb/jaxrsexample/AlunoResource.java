
package br.edu.uepb.jaxrsexample;

import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

// The Java class will be hosted at the URI path "/aluno"
@Path("/alunos")
public class AlunoResource {
	
	private static AlunoRepository alunoRepository = new AlunoRepository();
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getAlunos() {
        return Response.ok(alunoRepository.getAll()).build();
    }
    
    @POST
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createAluno(Aluno aluno) {
    	alunoRepository.create(aluno);
    	return Response.status(Response.Status.CREATED)
    			.entity(aluno).build();
    }
    
    @GET
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getAlunoById(@PathParam("id") long id) {
    	return Response.ok(alunoRepository.getById(id)).build();
    }
    
    @PUT
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response editAluno(@PathParam("id") long id, Aluno aluno) {
    	Aluno a = alunoRepository.getById(id);
    	if(a == null)
    		return Response.status(Response.Status.NOT_FOUND).build();
    	try {
    		aluno.setId(id);
    		alunoRepository.edit(aluno);
    		return Response.ok(aluno).build();
    	} catch(Exception e) {
    		return Response
    				.status(Response.Status.INTERNAL_SERVER_ERROR)
    				.entity(e.getMessage()).build();
    	}
    }
    
    @DELETE
    @Path("{id}")
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response deleteAluno(@PathParam("id") long id, Aluno aluno) {
    	Aluno a = alunoRepository.getById(id);
    	if(a == null)
    		return Response.status(Response.Status.NOT_FOUND).build();
    	try {
    		alunoRepository.delete(aluno.getId());
    		return Response.noContent().build();
    	} catch(Exception e) {
    		return Response
    				.status(Response.Status.INTERNAL_SERVER_ERROR)
    				.entity(e.getMessage()).build();
    	}
    }
}
