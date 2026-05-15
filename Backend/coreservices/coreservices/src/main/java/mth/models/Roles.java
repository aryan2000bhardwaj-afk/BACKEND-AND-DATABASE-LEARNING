package mth.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="roles")
public class Roles {
	@Id
	Long Role;
	String rolename;
	public Long getRole() {
		return Role;
	}
	public void setRole(Long role) {
		Role = role;
	}
	public String getRolename() {
		return rolename;
	}
	public void setRolename(String rolename) {
		this.rolename = rolename;
	}
	@Override
	public String toString() {
		return "Roles [Role=" + Role + ", rolename=" + rolename + "]";
	}
	

}
