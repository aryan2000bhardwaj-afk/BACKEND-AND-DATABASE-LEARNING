package mth.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import mth.models.Users;

@Repository
public interface UserRepository extends JpaRepository<Users, Long> {
	
	@Query("select U.id from Users U where U.email=:email")
	public Object checkByEmail(@Param("email") String email);

	@Query("select U.role from Users U where U.email=:username")
	public Object validateCredentials(@Param("username") String username ,@Param("password") String password);

	
	@Query("select U from Users U where U.email=:email")
	public Object findByEmail(@Param("email") String email);
	
	@Query("select M from Menus M join Rolemapping R on M.mid=R.mid where R.role=:role order by M.mid")
	public List<Object> getMenus(@Param("role") Long role);
}
