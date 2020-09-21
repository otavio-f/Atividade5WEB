package br.edu.uepb.jaxrsexample;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class TurmaRepository {
	
	private static HashSet<Turma> turmas = new HashSet<Turma>();
	
	public List<Turma> getAll(){
		return new ArrayList<Turma>(turmas);
	}
	
	public void create(Turma a) {
		if(a.getId()==0)
			a.setId(genId(turmas.size()+1));
		turmas.add(a);
	}
	
	public boolean containsId(long id) {
		for(Turma a: turmas)
			if(a.getId()==id)
				return true;
		return false;
	}
	
	public long genId(final long possible) {
		if(this.containsId(possible))
			return genId(possible+1);
		return possible;
	}
	
	public Turma getById(long id) {
		for(Turma a: turmas)
			if(a.getId()==id)
				return a;
		return null;
	}
	
	public void edit(Turma a) {
		turmas.remove(getById(a.getId()));
		turmas.add(a);
	}
	
	public void delete(long id) {
		turmas.remove(id);
	}
}
