select ps.product_sales_id,
	ps.sales_year,
    tl.sales_team_lead,
    tl.region,
    ii.product_name,
    ii.price,
	sum(ps.sales_quantity) as total_qty_sold, 
	ps.sales_quantity * ii.price as total_product, 
	ps.sales_quantity * ii.warranty_price as total_warranty,
	(ps.sales_quantity * ii.price) + (ps.sales_quantity * ii.warranty_price) as total_sales
from team_lead tl cross join product_sales ps
	on tl.emp_id = ps.emp_id
	cross join item_info ii
	on ps.item_code = ii.prod_code
group by ps.product_sales_id;