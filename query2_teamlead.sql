select tl.sales_team_lead,
	sum(ps.sales_quantity) as total_qty_sold, 
	ps.sales_quantity * ii.price as total_product, 
	ps.sales_quantity * ii.warranty_price as total_warranty,
	(ps.sales_quantity * ii.price) + (ps.sales_quantity * ii.warranty_price) as total_sales
from item_info ii cross join product_sales ps
	on ps.item_code = ii.prod_code
	cross join team_lead tl 
	on ps.emp_id = tl.emp_id
group by sales_team_lead;