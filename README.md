# learn-by-doing


  1)   CLOUD 
  
            AWS :                   1. AWS SysOps Associate
                                    2. AWS Devleoper Associate
                                    
            CLOUD FOUNDRY :         1. CF BEGINNERS
                                    2. CF INTERMEDIATE 

  2)   DEVELOPER : 
          
            PYTHON :                1. PYTHON
                                    2. FLASK
                                    3. DJANGO  
                                    4. DESIGN PATTERN    
           
            JAVA :                  1. CORE JAVA 
                                    2. REST 
                                    3. SPRING  
                                    4. DESIGN PATTERN            
            
            UI :                    1. REACTJS 
                                    2. REDUX 
                                    3. CSS
                                    4. JAVA SCRIPT
      
  3)  DEV OPS  :
    
          Version Control & Build Management :
                           1. GIT
                           2. MAVEN
                           3. GRADLE
                           4. NODE
                           5. PIP
                           
         
          Orchestration & Containerization & Configuration :
                           1. JENKINS
                           2. DOCKER
                           3. KUBERNETES
                           4. PUPPET
                           5. ANSIBLE
                           
                                           
          Loggin & Streaming : 
                           1. Apache KAFKA
                           2. Apache SPARK
                                           
  
    
  Cloud - Training 
  
  Others -Tech Primers & Reference Documentation 
  
  
  const ReactTable = window.ReactTable.default;
  
  class MyTable extends React.Component {
  	constructor(props) {
  		super(props);
  
  		this.state = { selected: {}, selectAll: 0, data: makeData() };
  
  		this.toggleRow = this.toggleRow.bind(this);
  	}
  
  	toggleRow(firstName) {
  		const newSelected = Object.assign({}, this.state.selected);
  		newSelected[firstName] = !this.state.selected[firstName];
  		this.setState({
  			selected: newSelected,
  			selectAll: 2
  		});
  	}
  
  	toggleSelectAll() {
  		let newSelected = {};
  
  		if (this.state.selectAll === 0) {
  			this.state.data.forEach(x => {
  				newSelected[x.firstName] = true;
  			});
  		}
  
  		this.setState({
  			selected: newSelected,
  			selectAll: this.state.selectAll === 0 ? 1 : 0
  		});
  	}
  
  	render() {
  		const columns = [
  			{
  				Header: "#POOL",
  				columns: [
  					{
  						id: "checkbox",
  						accessor: "",
  						Cell: ({ original }) => {
  							return (
  								<input
  									type="checkbox"
  									className="checkbox"
  									checked={this.state.selected[original.applicationName] === true}
  									onChange={() => this.toggleRow(original.applicationName)}
  								/>
  							);
  						},
  						Header: x => {
  							return (
  								<input
  									type="checkbox"
  									className="checkbox"
  									checked={this.state.selectAll === 1}
  									ref={input => {
  										if (input) {
  											input.indeterminate = this.state.selectAll === 2;
  										}
  									}}
  									onChange={() => this.toggleSelectAll()}
  								/>
  							);
  						},
  						sortable: false,
  						width: 45
  					},
  					{
  						Header: "Application Name",
  						accessor: "applicationName"
  					},
  					{
  						Header: "Status",
  						id: "status",
  						accessor: d => d.status
  					}
  				]
  			}
  			
  		];
  
  		return (
  			<div>
  				<ReactTable
  					data={this.state.data}
  					columns={columns}
  					defaultSorted={[{ id: "applicationName", desc: false }]}
  				/>
  			</div>
  		);
  	}
  }
  
  ReactDOM.render(<MyTable />, document.getElementById("root"));
  
  function makeData() {
  	return [
  		{
  			applicationName: "judge",
  			status: "babies",
  			age: 16
  		}  		
  	];
  }
           